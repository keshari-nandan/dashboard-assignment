"use client";

import { useContext, useEffect, useState } from "react";
import Link from "next/link";
import { useRouter } from "next/navigation";
import { isAutheitcated, removeToken, getUser } from "@/lib/auth";
import { RightDrawerContext } from "@/context/drawer-context";
import WidgetForm from "../Pages/Dashboard/forms/WidgetForm";

const Navbar = () => {
    const [user, setUser] = useState({});
    const router = useRouter();
    const [autheiticated, setAutheiticated] = useState(false);
    const context = useContext(RightDrawerContext);

    useEffect(() => {
        getUser().then((user) => setUser(user));
        isAutheitcated().then((autheiticated) => setAutheiticated(autheiticated));
    }, [])


    const openDrawer = () => {
        context.openDrawer({
            isOpen: true,
            title: 'Add Widget',
            children: <WidgetForm />,
            width: 'lg:w-2/5 xl:w-1/3'
        });
    }

    return (
        <header className="antialiased">
            <nav className="bg-white border-gray-200 px-4 lg:px-6 py-2.5 dark:bg-gray-800">
                <div className="flex flex-wrap justify-between items-center">
                    <div className="flex justify-start items-center">
                        <Link href="/" className="flex mr-4">
                            <span className="self-center text-2xl font-semibold whitespace-nowrap dark:text-white">Artica</span>
                        </Link>
                        {autheiticated && user ? (
                            <Link href="/dashboard" className="flex mr-4">
                            <span className="self-center font-semibold whitespace-nowrap dark:text-white">Dashboard</span>
                        </Link>
                        ) : null}
                        
                    </div>
                    <div className="flex items-center lg:order-2">
                        
                        {autheiticated && user ? (
                            <>
                            <button onClick={openDrawer} type="button" className="sm:inline-flex items-center justify-center text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:ring-primary-300 font-medium rounded-lg text-xs px-3 py-2 mr-2 dark:bg-primary-600 dark:hover:bg-primary-700 focus:outline-none dark:focus:ring-primary-800">
                                Add Widget</button>

                            {user?.first_name && (
                                <>
                                <button  type="button" className="sm:inline-flex items-center justify-center text-primary-500 bg-gray-100  font-medium rounded-lg text-xs px-3 py-2 mr-2 focus:outline-none ">
                                Welcome {user?.first_name + ' ' + user?.last_name}
                                </button>
                                </>
                            )}
                            
                            <button onClick={() => {
                                removeToken();
                                router.push('/');
                                }}  type="button" className="sm:inline-flex items-center justify-center text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:ring-primary-300 font-medium rounded-lg text-xs px-3 py-2 mr-2 dark:bg-primary-600 dark:hover:bg-primary-700 focus:outline-none dark:focus:ring-primary-800">
                                Logout</button>
                            </>
                        ) : (
                            <>
                            <Link href="/auth/login" type="button" className="sm:inline-flex items-center justify-center text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:ring-primary-300 font-medium rounded-lg text-xs px-3 py-2 mr-2 dark:bg-primary-600 dark:hover:bg-primary-700 focus:outline-none dark:focus:ring-primary-800">
                                Login</Link>
                            </>
                        )}
                        
                        
                    </div>
                </div>
            </nav>
            </header>
    )
}

export default Navbar;