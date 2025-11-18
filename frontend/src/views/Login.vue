<script setup>
import { ref } from "vue";
import { useRouter } from "vue-router";
import { useAuthStore } from "@/stores/auth";

const router = useRouter();
const authStore = useAuthStore();

const username = ref("");
const password = ref("");
const error = ref("");
const loading = ref(false);

const handleLogin = async () => {
  error.value = "";

  if (!username.value || !password.value) {
    error.value = "Username dan password wajib diisi";
    return;
  }

  loading.value = true;
  try {
    const result = await authStore.login(username.value, password.value);
    if (result.success) {
      router.push("/dashboard");
    } else {
      error.value = result.message;
    }
  } catch (err) {
    error.value = "Terjadi kesalahan koneksi ke server";
  } finally {
    loading.value = false;
  }
};
</script>

<template>
  <div
    class="min-h-screen w-full flex items-center justify-center bg-linear-to-br from-orange-50 to-orange-100 p-4"
  >
    <div
      class="bg-white w-full max-w-md rounded-2xl shadow-xl overflow-hidden border border-orange-100"
    >
      <div class="bg-orange-500 p-8 text-center">
        <h1 class="text-3xl font-bold text-white tracking-wide">Horus Tito</h1>
        <p class="text-orange-100 mt-2 text-sm">User Management System</p>
      </div>

      <div class="p-8">
        <h2 class="text-2xl font-semibold text-gray-800 mb-6 text-center">
          Selamat Datang Kembali
        </h2>

        <form @submit.prevent="handleLogin" class="space-y-5">
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-1"
              >Username</label
            >
            <input
              v-model="username"
              type="text"
              class="w-full px-4 py-3 rounded-lg border border-gray-300 focus:ring-2 focus:ring-orange-500 focus:border-orange-500 transition-all outline-none"
              placeholder="Masukan username anda"
            />
          </div>

          <div>
            <label class="block text-sm font-medium text-gray-700 mb-1"
              >Password</label
            >
            <input
              v-model="password"
              type="password"
              class="w-full px-4 py-3 rounded-lg border border-gray-300 focus:ring-2 focus:ring-orange-500 focus:border-orange-500 transition-all outline-none"
              placeholder="••••••••"
            />
          </div>

          <div
            v-if="error"
            class="p-3 rounded-lg bg-red-50 text-red-600 text-sm border border-red-200 flex items-center gap-2"
          >
            <svg
              xmlns="http://www.w3.org/2000/svg"
              class="h-5 w-5"
              viewBox="0 0 20 20"
              fill="currentColor"
            >
              <path
                fill-rule="evenodd"
                d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7 4a1 1 0 11-2 0 1 1 0 012 0zm-1-9a1 1 0 00-1 1v4a1 1 0 102 0V6a1 1 0 00-1-1z"
                clip-rule="evenodd"
              />
            </svg>
            {{ error }}
          </div>

          <button
            type="submit"
            :disabled="loading"
            class="w-full bg-orange-600 hover:bg-orange-700 text-white font-bold py-3 px-4 rounded-lg shadow-lg hover:shadow-orange-500/30 transition-all duration-200 disabled:opacity-70 disabled:cursor-not-allowed flex justify-center items-center"
          >
            <span
              v-if="loading"
              class="w-5 h-5 border-2 border-white border-t-transparent rounded-full animate-spin mr-2"
            ></span>
            {{ loading ? "Memproses..." : "Masuk Sekarang" }}
          </button>
        </form>

        <div class="mt-6 text-center">
          <p class="text-gray-600 text-sm">
            Belum punya akun?
            <router-link
              to="/register"
              class="text-orange-600 hover:text-orange-700 font-semibold hover:underline"
            >
              Daftar Disini
            </router-link>
          </p>
        </div>
      </div>
    </div>
  </div>
</template>
