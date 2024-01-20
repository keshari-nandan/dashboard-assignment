"use client";

import { useState } from "react";
import { getToken } from "@/lib/auth";
import toast from "react-hot-toast";

const WidgetForm = () => {
    const [loading, setLoading] = useState(false);
    const [name, setName] = useState('');
    const [type, setType] = useState('stats');
    const [measure, setMeasure] = useState('sum');
    const [dimension, setDimension] = useState('');


    const onFormSubmit = async(e) => {
        e.preventDefault();
        setLoading(true);
        const data = {
            name: name,
            type: type,
            measure: measure,
            dimension: dimension
        }
        const token = await getToken();
        const resp = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/widgets`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${token}`
            },
            body: JSON.stringify(data)
        })

        const json = await resp.json();

        if(json.ok) {
            toast.success("Widget has been saved successfully.");
            setName('');
            setType('');
            setAggregator('');
        } else {
            toast.error(json.detail ?? "Something went wrong.");
        }
        setLoading(false);
    }

    return (
        <>
       <div className="p-6 space-y-4 md:space-y-6 sm:p-8">
            <form method="post" className="space-y-4 md:space-y-6" action="#" onSubmit={onFormSubmit}>
                <div className="w-full">
                    <label htmlFor="name" className="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Widget Name</label>
                    <input onKeyUp={(e) => setName(e.target.value)} type="text" id="name" className="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="Total Spend" required="" />
                </div>
                <div className="w-full">
                        <label htmlFor="dimension" className="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Dimension</label>
                        <select onChange={(e) => setDimension(e.target.value)} id="dimension" className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">
                        <option value={""}>Select Dimension</option>
                        <option value={"payment_mode"}>Payment Mode</option>
                            <option value={"category"}>Category</option>
                            <option value={"card"}>Card</option>
                            <option value={"bank"}>Bank</option>
                            <option value={"tag"}>Tag</option>
                        </select>
                    </div>
                <div className="flex justify-between gap-2">
                    <div className="w-full">
                        <label htmlFor="widget_type" className="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Widget Type</label>
                        <select onChange={(e) => setType(e.target.value)} id="widget_type" className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">
                            <option value={"Stats"}>Stats</option>
                            <option value={"Pie"}>Pie Chart</option>
                        </select>
                    </div>
                    <div className="w-full">
                        <label htmlFor="measure" className="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Measures</label>
                        <select onChange={(e) => setMeasure(e.target.value)} id="measure" className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">
                            <option value={"sum"}>Sum</option>
                            <option value={"svg"}>Average</option>
                            <option value={"cound"}>Count</option>
                            <option value={"min"}>Min</option>
                            <option value={"max"}>Max</option>
                        </select>
                    </div>
                </div>
                <button type="submit" className="w-full text-white bg-primary-500 hover:bg-primary-700 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800">{loading ? "Please wait..." : "Save"}</button>
            </form>
        </div>
        </>
    );
}

export default WidgetForm;