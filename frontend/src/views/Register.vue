<script setup>
import { ref } from "vue";
import { useRouter } from "vue-router";
import api from "@/services/api";

const router = useRouter();

const formData = ref({
  nama: "",
  email: "",
  username: "",
  password: "",
});

const error = ref("");
const success = ref("");
const loading = ref(false);

const validateEmail = (email) => {
  const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return regex.test(email);
};

const handleRegister = async () => {
  error.value = "";
  success.value = "";

  // Validasi client-side
  if (
    !formData.value.nama ||
    !formData.value.email ||
    !formData.value.username ||
    !formData.value.password
  ) {
    error.value = "Semua field harus diisi";
    return;
  }

  if (!validateEmail(formData.value.email)) {
    error.value = "Format email tidak valid";
    return;
  }

  if (formData.value.password.length < 6) {
    error.value = "Password minimal 6 karakter";
    return;
  }

  loading.value = true;

  try {
    const response = await api.post("/users/register", formData.value);
    success.value = response.data.message;

    setTimeout(() => {
      router.push("/login");
    }, 1500);
  } catch (err) {
    error.value = err.response?.data?.error || "Registrasi gagal";
  } finally {
    loading.value = false;
  }
};
</script>

<template>
  <div
    class="min-h-screen flex items-center justify-center bg-linear-to-br from-orange-400 to-orange-600 py-12 px-4"
  >
    <div class="bg-white rounded-lg shadow-xl p-8 w-full max-w-md">
      <div class="text-center mb-8">
        <h1 class="text-3xl font-bold text-orange-600">Registrasi Akun</h1>
        <p class="text-gray-600 mt-2">Buat akun baru Anda</p>
      </div>

      <form @submit.prevent="handleRegister" class="space-y-4">
        <div>
          <label
            for="nama"
            class="block text-sm font-medium text-gray-700 mb-2"
          >
            Nama Lengkap
          </label>
          <input
            id="nama"
            v-model="formData.nama"
            type="text"
            required
            class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-orange-500 focus:border-transparent"
            placeholder="Nama lengkap Anda"
          />
        </div>

        <div>
          <label
            for="email"
            class="block text-sm font-medium text-gray-700 mb-2"
          >
            Email
          </label>
          <input
            id="email"
            v-model="formData.email"
            type="email"
            required
            class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-orange-500 focus:border-transparent"
            placeholder="email@example.com"
          />
        </div>

        <div>
          <label
            for="username"
            class="block text-sm font-medium text-gray-700 mb-2"
          >
            Username
          </label>
          <input
            id="username"
            v-model="formData.username"
            type="text"
            required
            class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-orange-500 focus:border-transparent"
            placeholder="Username unik"
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
            v-model="formData.password"
            type="password"
            required
            class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-orange-500 focus:border-transparent"
            placeholder="Min. 6 karakter"
          />
        </div>

        <div
          v-if="error"
          class="p-3 bg-red-100 border border-red-400 text-red-700 rounded-lg text-sm"
        >
          {{ error }}
        </div>

        <div
          v-if="success"
          class="p-3 bg-green-100 border border-green-400 text-green-700 rounded-lg text-sm"
        >
          {{ success }}
        </div>

        <button
          type="submit"
          :disabled="loading"
          class="w-full bg-orange-500 text-white py-2 px-4 rounded-lg hover:bg-orange-600 focus:outline-none focus:ring-2 focus:ring-orange-500 focus:ring-offset-2 disabled:opacity-50 disabled:cursor-not-allowed font-semibold"
        >
          {{ loading ? "Mendaftar..." : "Daftar" }}
        </button>
      </form>

      <div class="mt-6 text-center">
        <p class="text-sm text-gray-600">
          Sudah punya akun?
          <router-link
            to="/login"
            class="text-orange-600 hover:text-orange-700 font-semibold"
          >
            Login di sini
          </router-link>
        </p>
      </div>
    </div>
  </div>
</template>
