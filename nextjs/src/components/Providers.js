"use client";
import { RightDrawerProvider } from '@/context/drawer-context';
import CubeProvider from '@/components/Providers/CubeProvider';
import {Toaster} from "react-hot-toast";

const Providers = ({children}) => {
    return (
        <>
        <RightDrawerProvider>
            <CubeProvider>
                {children}
            </CubeProvider>
            <Toaster position="top-right"/>
        </RightDrawerProvider>
        </>
    );
}

export default Providers;