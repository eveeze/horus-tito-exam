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
    error.value = "Username dan password harus diisi";
    return;
  }

  loading.value = true;

  const result = await authStore.login(username.value, password.value);

  loading.value = false;

  if (result.success) {
    router.push("/dashboard");
  } else {
    error.value = result.message;
  }
};
</script>

<template>
  <div
    class="min-h-screen flex items-center justify-center bg-linear-to-br from-orange-400 to-orange-600"
  >
    <div class="bg-white rounded-lg shadow-xl p-8 w-full max-w-md">
      <div class="text-center mb-8">
        <h1 class="text-3xl font-bold text-orange-600">User Management</h1>
        <p class="text-gray-600 mt-2">Horus Theme</p>
      </div>

      <form @submit.prevent="handleLogin" class="space-y-6">
        <div>
          <label
            for="username"
            class="block text-sm font-medium text-gray-700 mb-2"
          >
            Username
          </label>
          <input
            id="username"
            v-model="username"
            type="text"
            required
            class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-orange-500 focus:border-transparent"
            placeholder="Masukkan username"
          />
        </div>

        <div>
          <label
            for="password"
            class="block text-sm font-medium text-gray-700 mb-2"
          >
            Password
          </label>
          <input
            id="password"
            v-model="password"
            type="password"
            required
            class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-orange-500 focus:border-transparent"
            placeholder="Masukkan password"
          />
        </div>

        <div
          v-if="error"
          class="p-3 bg-red-100 border border-red-400 text-red-700 rounded-lg text-sm"
        >
          {{ error }}
        </div>

        <button
          type="submit"
          :disabled="loading"
          class="w-full bg-orange-500 text-white py-2 px-4 rounded-lg hover:bg-orange-600 focus:outline-none focus:ring-2 focus:ring-orange-500 focus:ring-offset-2 disabled:opacity-50 disabled:cursor-not-allowed font-semibold"
        >
          {{ loading ? "Loading..." : "Login" }}
        </button>
      </form>

      <div class="mt-6 text-center">
        <p class="text-sm text-gray-600">
          Belum punya akun?
          <router-link
            to="/register"
            class="text-orange-600 hover:text-orange-700 font-semibold"
          >
            Daftar di sini
          </router-link>
        </p>
      </div>
    </div>
  </div>
</template>
