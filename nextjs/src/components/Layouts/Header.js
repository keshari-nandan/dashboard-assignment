import Navbar from "./Navbar";


const Header = ({children}) => {
    return (
        <>
            <Navbar />
        {children}
        </>
    );  
};

export default Header;