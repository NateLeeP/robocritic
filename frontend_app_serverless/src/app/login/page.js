const LoginForm = () => {
    return (
        <div className="flex flex-col items-center justify-center h-screen bg-gray-100">
            <div className="bg-white p-8 rounded-lg shadow-md">
                <h1 className="text-2xl font-bold mb-4">Welcome to TaskList Pro</h1>
                <div className="mb-4">
                    <label htmlFor="email" className="block font-medium mb-2">
                        Enter your email address to get started
                    </label>
                    <input
                        type="email"
                        id="email"
                        className="w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                        placeholder="name@yourcompany.com"
                    />
                </div>
                <button className="bg-blue-500 text-white px-4 py-2 rounded-md hover:bg-blue-600 transition-colors duration-300 w-full mb-4">
                    Continue with Email
                </button>
                <div className="flex justify-center space-x-4 mb-4">
                    <button className="bg-white text-gray-700 px-4 py-2 rounded-md border border-gray-300 hover:bg-gray-100 transition-colors duration-300">
                        Continue with Google
                    </button>
                    <button className="bg-black text-white px-4 py-2 rounded-md hover:bg-gray-800 transition-colors duration-300">
                        Continue with Apple
                    </button>
                </div>
                <p className="text-center text-gray-500">
                    Already have an account?{' '}
                    <a href="#" className="text-blue-500 hover:underline">
                        Sign In
                    </a>
                </p>
            </div>
        </div>
    );
};

export default LoginForm;