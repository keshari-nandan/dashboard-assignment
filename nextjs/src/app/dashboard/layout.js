
import Header from "@/components/Layouts/Header";

const DashboardLayput = ({children}) => {
    return (
        <>
        <Header />
        <div className="px-10 bg-gray-100">
            {children}
        </div>
        </>
    );
}
export default DashboardLayput;