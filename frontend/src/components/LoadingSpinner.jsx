function LoadingSpinner() {

  return (

    <div className="fixed inset-0 bg-black/40 backdrop-blur-sm flex justify-center items-center z-50">

      <div className="bg-white rounded-3xl p-10 text-center shadow-2xl">

        <div className="w-16 h-16 border-4 border-indigo-500 border-t-transparent rounded-full animate-spin mx-auto"></div>

        <h2 className="text-2xl font-bold mt-6">

          Generating Learning Path...

        </h2>

        <p className="text-gray-500 mt-2">

          AI is preparing your roadmap.

        </p>

      </div>

    </div>

  )

}

export default LoadingSpinner