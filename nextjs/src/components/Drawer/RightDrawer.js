import classNames from "classnames";

const RightDrawer = ({title, open, onClose, children, width = "w-96"}) => {
    return (
        <>
            <div
                className={classNames(open ? '' : 'translate-x-full', "fixed right-0 z-50 shadow overflow-y-auto h-full border-r transition-transform bg-white dark:bg-gray-800 w-full " + width)}>
                <div className="border-b overflow-auto justify-between px-4 py-2 flex items-center border-gray-200 dark:border-gray-700">
                    <div>
                        <h5
                            className="inline-flex items-center text-base font-semibold text-gray-500 dark:text-white">
                            {title ?? 'Manage'}
                        </h5>
                    </div>
                    <div>
                        <button type="button"
                                onClick={onClose}
                                className="text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm w-8 h-8 inline-flex items-center justify-center dark:hover:bg-gray-600 dark:hover:text-white">
                            <svg className="w-3 h-3" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none"
                                 viewBox="0 0 14 14">
                                <path stroke="currentColor" strokeLinecap="round" strokeLinejoin="round" strokeWidth="2"
                                      d="m1 1 6 6m0 0 6 6M7 7l6-6M7 7l-6 6"/>
                            </svg>
                            <span className="sr-only">Close menu</span>
                        </button>
                    </div>

                </div>
                {children}
            </div>
        </>

    )
}

export default RightDrawer