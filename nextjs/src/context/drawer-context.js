"use client";
import {createContext, useState} from "react";
import RightDrawer from "@/components/Drawer/RightDrawer";
import classNames from "classnames";


export const RightDrawerContext = createContext(undefined);

export function RightDrawerProvider({children}) {
    const [drawer, handleDrawer] = useState({isOpen: false, title: 'Manage', children: null, width: 'w-96'});

    const openDrawer = (drawer) => {
        handleDrawer({...drawer, isOpen: true});
    }

    const closeDrawer = () => {
        handleDrawer({...drawer, isOpen: false, children: null, title: 'Manage'});
    }

    return (
        <RightDrawerContext.Provider value={{drawer, openDrawer, closeDrawer}}>
            <RightDrawer width={drawer.width} open={drawer.isOpen} title={drawer.title} onClose={closeDrawer}>
                {drawer.children && drawer.children}
            </RightDrawer>
            <div>
                {drawer.isOpen && <div
                    className="fixed pointer-events-none inset-0 bg-gray-500 bg-opacity-75 transition-opacity"/>}
                <div
                    className={classNames(drawer.isOpen ? 'opacity-25 z-0 disabled-background pointer-events-none' : '')}>
                    {children}
                </div>
            </div>
        </RightDrawerContext.Provider>
    )
}