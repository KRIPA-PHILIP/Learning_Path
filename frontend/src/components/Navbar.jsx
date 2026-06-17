function Navbar() {

    return (

        <nav className="bg-white shadow-sm sticky top-0 z-50">

            <div className="max-w-7xl mx-auto px-6 py-5 flex justify-between items-center">

                <div>

                    <h2 className="text-2xl font-bold gradient-text">

                        LearnFlow AI

                    </h2>

                </div>

                <div className="hidden md:flex gap-8 text-gray-600">

                    <a href="#">Home</a>

                    <a href="#">Features</a>

                    <a href="#">About</a>

                </div>

            </div>

        </nav>

    )

}

export default Navbar;