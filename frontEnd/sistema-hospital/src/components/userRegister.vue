<!-- <template>
    <section class="bg-gray-100 min-h-screen flex box-border justify-center items-center">
    <div class="bg-[#dfa674] rounded-2xl flex max-w-3xl p-5 items-center">
        <div class="md:w-1/2 px-8">
            <h2 class="font-bold text-3xl text-[#002D74]">Registro Personas</h2>

            <form action="" class="flex flex-col gap-4">
                <input class="p-2 mt-8 rounded-xl border" type="text" name="nombre" placeholder="Nombre">
                <input class="p-2 rounded-xl border" type="text" name="primerApellido" placeholder="Primer Apellido">
                <input class="p-2 rounded-xl border" type="text" name="segundoApellido" placeholder="Segundo Apellido">
                <input class="p-2 rounded-xl border" type="text" name="segundoApellido" placeholder="CURP">
                <input class="p-2 rounded-xl border" type="text" name="segundoApellido" placeholder="Genero">
                <input class="p-2 rounded-xl border" type="text" name="segundoApellido" placeholder="Sangre">
                <input class="p-2 rounded-xl border" type="text" name="segundoApellido" placeholder="Fecha Nacimiento">
                <input class="p-2 rounded-xl border" type="text" name="segundoApellido" placeholder="Telefono">
                <input class="p-2 rounded-xl border" type="email" name="segundoApellido" placeholder="Correo">
                <input class="p-2 rounded-xl border w-full" type="password" name="password" id="password" placeholder="Nombre Usuario">
                <input class="p-2 rounded-xl border w-full" type="password" name="password" id="password" placeholder="Contraseña">

                <div class="relative">
                    
                    <input class="p-2 rounded-xl border w-full" type="password" name="password" id="password" placeholder="Confirmar contraseña">
                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="gray" id="togglePassword"
                        class="bi bi-eye absolute top-1/2 right-3 -translate-y-1/2 cursor-pointer z-20 opacity-100"
                        viewBox="0 0 16 16">
                        <path
                            d="M16 8s-3-5.5-8-5.5S0 8 0 8s3 5.5 8 5.5S16 8 16 8zM1.173 8a13.133 13.133 0 0 1 1.66-2.043C4.12 4.668 5.88 3.5 8 3.5c2.12 0 3.879 1.168 5.168 2.457A13.133 13.133 0 0 1 14.828 8c-.058.087-.122.183-.195.288-.335.48-.83 1.12-1.465 1.755C11.879 11.332 10.119 12.5 8 12.5c-2.12 0-3.879-1.168-5.168-2.457A13.134 13.134 0 0 1 1.172 8z">
                        </path>
                        <path
                            d="M8 5.5a2.5 2.5 0 1 0 0 5 2.5 2.5 0 0 0 0-5zM4.5 8a3.5 3.5 0 1 1 7 0 3.5 3.5 0 0 1-7 0z">
                        </path>
                    </svg>
                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor"
                        class="bi bi-eye-slash-fill absolute top-1/2 right-3 -z-1 -translate-y-1/2 cursor-pointer hidden"
                        id="mama" viewBox="0 0 16 16">
                        <path
                            d="m10.79 12.912-1.614-1.615a3.5 3.5 0 0 1-4.474-4.474l-2.06-2.06C.938 6.278 0 8 0 8s3 5.5 8 5.5a7.029 7.029 0 0 0 2.79-.588zM5.21 3.088A7.028 7.028 0 0 1 8 2.5c5 0 8 5.5 8 5.5s-.939 1.721-2.641 3.238l-2.062-2.062a3.5 3.5 0 0 0-4.474-4.474L5.21 3.089z">
                        </path>
                        <path
                            d="M5.525 7.646a2.5 2.5 0 0 0 2.829 2.829l-2.83-2.829zm4.95.708-2.829-2.83a2.5 2.5 0 0 1 2.829 2.829zm3.171 6-12-12 .708-.708 12 12-.708.708z">
                        </path>
                    </svg>
                </div>
                <button class="bg-[#002D74] text-white py-2 rounded-xl hover:scale-105 duration-300 hover:bg-[#206ab1] font-medium" type="submit">Registrar Usuario</button>
            </form>
            <RouterLink to="/">
            <div class="mt-10 text-sm border-b border-gray-500 py-5 playfair tooltip">Forget password?</div>
        </RouterLink>
            <div class="mt-4 text-sm flex justify-between items-center container-mr">
                <p class="mr-3 md:mr-0 ">If you don't have an account..</p>
                <button class="hover:border register text-white bg-[#002D74] hover:border-gray-400 rounded-xl py-2 px-5 hover:scale-110 hover:bg-[#002c7424] font-semibold duration-300">Register</button>
            </div>
        </div>
        <div class="md:block hidden w-1/2">
            <img class="rounded-2xl max-h-[1600px]" src="https://images.unsplash.com/photo-1552010099-5dc86fcfaa38?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3w0NzEyNjZ8MHwxfHNlYXJjaHwxfHxmcmVzaHxlbnwwfDF8fHwxNzEyMTU4MDk0fDA&ixlib=rb-4.0.3&q=80&w=1080" alt="login form image">
        </div>
    </div>
</section>
</template> -->

<template>
    <!-- source: https://gist.github.com/nraloux/bce10c4148380061781b928cdab9b193 -->
<!-- I have added support for dark mode and improved UI -->

<div class="h-full bg-gray-400 dark:bg-gray-900">
	<!-- Container -->
	<div class="mx-auto">
		<div class="flex justify-center px-6 py-12">
			<!-- Row -->
			<div class="w-full xl:w-3/4 lg:w-11/12 flex">
				<!-- Col -->
				<div class="w-full h-auto bg-gray-400 dark:bg-gray-800 hidden lg:block lg:w-5/12 bg-cover rounded-l-lg"
					style="background-image: url('https://previews.123rf.com/images/dotshock/dotshock1511/dotshock151102041/48036190-grupo-de-personal-m%C3%A9dico-en-el-hospital-el-equipo-de-m%C3%A9dicos-de-pie-juntos.jpg')"></div>
				<!-- Col -->
				<div class="w-full lg:w-7/12 bg-white dark:bg-gray-700 p-5 rounded-lg lg:rounded-l-none">
					<h3 class="py-4 text-2xl text-center text-gray-800 dark:text-white">Registro</h3>
					<form class="px-8 pt-6 pb-8 mb-4 bg-white dark:bg-gray-800 rounded">
						<div class="mb-4 md:flex md:justify-between">
							<div class="mb-4 md:mr-2 md:mb-0">
								<label class="block mb-2 text-sm font-bold text-gray-700 dark:text-white" for="name">
                                    Nombre
                                </label>
								<input
                                    class="w-full px-3 py-2 text-sm leading-tight text-gray-700 dark:text-white border rounded shadow appearance-none focus:outline-none focus:shadow-outline"
                                    id="name"
                                    type="text"
                                    placeholder="Nombre"
                                />
							</div>

                            <div class="mb-4 md:mr-2 md:mb-0">
								<label class="block mb-2 text-sm font-bold text-gray-700 dark:text-white" for="primerApellido">
                                    Primer Apellido
                                </label>
								<input
                                    class="w-full px-3 py-2 text-sm leading-tight text-gray-700 dark:text-white border rounded shadow appearance-none focus:outline-none focus:shadow-outline"
                                    id="primerApellido"
                                    type="text"
                                    placeholder="Primer Apellido"
                                />
							</div>

							<div class="md:ml-2">
								<label class="block mb-2 text-sm font-bold text-gray-700 dark:text-white" for="segundoApellido">
                                    Segundo Apellido
                                </label>
								<input
                                    class="w-full px-3 py-2 text-sm leading-tight text-gray-700 dark:text-white border rounded shadow appearance-none focus:outline-none focus:shadow-outline"
                                    id="segundoApellido"
                                    type="text"
                                    placeholder="Segundo Apellido"
                                />
							</div>
						</div>
                        <div class="mb-4 md:flex md:justify-between">
                            <div class="mb-4">
                                <label class="block mb-2 text-sm font-bold text-gray-700 dark:text-white" for="curp">
                                    CURP
                                </label>
                                <input
                                    class="w-full px-3 py-2 mb-3 text-sm leading-tight text-gray-700 dark:text-white border rounded shadow appearance-none focus:outline-none focus:shadow-outline"
                                    id="curp"
                                    type="text"
                                    placeholder="CURP"
                                />  
                            </div>

                            <div class="md:ml-2">
								<label class="block mb-2 text-sm font-bold text-gray-700 dark:text-white" for="genero">
                                    Género
                                </label>
								<input
                                    class="w-full px-3 py-2 text-sm leading-tight text-gray-700 dark:text-white border rounded shadow appearance-none focus:outline-none focus:shadow-outline"
                                    id="genero"
                                    type="text"
                                    placeholder="Género"
                                />
							</div>

                            <div class="md:ml-2">
								<label class="block mb-2 text-sm font-bold text-gray-700 dark:text-white" for="sangre">
                                    Sangre
                                </label>
								<input
                                    class="w-full px-3 py-2 text-sm leading-tight text-gray-700 dark:text-white border rounded shadow appearance-none focus:outline-none focus:shadow-outline"
                                    id="sangre"
                                    type="text"
                                    placeholder="Sangre"
                                />
							</div>
                        </div>

                        <div class="mb-4 md:flex md:justify-between">
                            <div class="mb-4">
                                <label class="block mb-2 text-sm font-bold text-gray-700 dark:text-white" for="curp">
                                    Fecha Nacimiento
                                </label>
                                <input
                                    class="w-full px-3 py-2 mb-3 text-sm leading-tight text-gray-700 dark:text-white border rounded shadow appearance-none focus:outline-none focus:shadow-outline"
                                    id="fechaNac"
                                    type="date"
                                    placeholder="Fecha Nacimiento"
                                />  
                            </div>

                            <div class="md:ml-2">
								<label class="block mb-2 text-sm font-bold text-gray-700 dark:text-white" for="telefono">
                                    Telefono
                                </label>
								<input
                                    class="w-full px-3 py-2 text-sm leading-tight text-gray-700 dark:text-white border rounded shadow appearance-none focus:outline-none focus:shadow-outline"
                                    id="telefono"
                                    type="text"
                                    placeholder="Telefono"
                                />
							</div>

                            <div class="md:ml-2">
								<label class="block mb-2 text-sm font-bold text-gray-700 dark:text-white" for="email">
                                    Correo
                                </label>
								<input
                                    class="w-full px-3 py-2 text-sm leading-tight text-gray-700 dark:text-white border rounded shadow appearance-none focus:outline-none focus:shadow-outline"
                                    id="email"
                                    type="email"
                                    placeholder="Correo"
                                />
							</div>
                        </div>

						<div class="mb-4 md:flex md:justify-between">
                            <div class="md:ml-2">
								<label class="block mb-2 text-sm font-bold text-gray-700 dark:text-white" for="user">
                                    Nombre Usuario
                                </label>
								<input
                                    class="w-full px-3 py-2 mb-3 text-sm leading-tight text-gray-700 dark:text-white border border-gray-500 rounded shadow appearance-none focus:outline-none focus:shadow-outline"
                                    id="user"
                                    type="text"
                                    placeholder="Nombre Usuario"
                                />
								
							</div>

							<div class="md:ml-2">
								<label class="block mb-2 text-sm font-bold text-gray-700 dark:text-white" for="password">
                                    Contraseña
                                </label>
								<input
                                    class="w-full px-3 py-2 mb-3 text-sm leading-tight text-gray-700 dark:text-white border border-gray-500 rounded shadow appearance-none focus:outline-none focus:shadow-outline"
                                    id="password"
                                    type="password"
                                    placeholder="******************"
                                />
							
							</div>
							<div class="md:ml-2">
								<label class="block mb-2 text-sm font-bold text-gray-700 dark:text-white" for="c_password">
                                    Confirmar Contraseña
                                </label>
								<input
                                    class="w-full px-3 py-2 mb-3 text-sm leading-tight text-gray-700 dark:text-white border rounded shadow appearance-none focus:outline-none focus:shadow-outline"
                                    id="c_password"
                                    type="password"
                                    placeholder="******************"
                                />
							</div>
						</div>
						<div class="mb-6 text-center">
							<button
                                class="w-full px-4 py-2 font-bold text-white bg-blue-500 rounded-full hover:bg-blue-700 dark:bg-blue-700 dark:text-white dark:hover:bg-blue-900 focus:outline-none focus:shadow-outline"
                                type="button"
                            >
                                Registrar Persona
                            </button>
						</div>
						<hr class="mb-6 border-t" />
						<div class="text-center">
							<a class="inline-block text-sm text-blue-500 dark:text-blue-500 align-baseline hover:text-blue-800"
								href="#">
								Forgot Password?
							</a>
						</div>
						<div class="text-center">
							<a class="inline-block text-sm text-blue-500 dark:text-blue-500 align-baseline hover:text-blue-800"
								href="./index.html">
								Already have an account? Login!
							</a>
						</div>
					</form>
				</div>
			</div>
		</div>
	</div>
</div>
</template>