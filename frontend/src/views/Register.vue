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

const validateForm = () => {
  if (
    !formData.value.nama ||
    !formData.value.email ||
    !formData.value.username ||
    !formData.value.password
  ) {
    return "Semua field wajib diisi";
  }
  if (formData.value.username.length < 3) return "Username minimal 3 karakter";
  if (formData.value.password.length < 6) return "Password minimal 6 karakter";
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  if (!emailRegex.test(formData.value.email)) return "Format email tidak valid";
  return null;
};

const handleRegister = async () => {
  error.value = "";
  success.value = "";

  const validationError = validateForm();
  if (validationError) {
    error.value = validationError;
    return;
  }

  loading.value = true;
  try {
    const response = await api.post("/users/register", formData.value);
    success.value = "Registrasi Berhasil! Mengalihkan ke login...";
    setTimeout(() => router.push("/login"), 2000);
  } catch (err) {
    error.value =
      err.response?.data?.error || "Gagal mendaftar. Silakan coba lagi.";
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
      <div class="p-8">
        <div class="text-center mb-8">
          <h1 class="text-3xl font-bold text-gray-800">Buat Akun Baru</h1>
          <p class="text-gray-500 mt-2">
            Bergabunglah dengan Horus Tito Management
          </p>
        </div>

        <form @submit.prevent="handleRegister" class="space-y-4">
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-1"
              >Nama Lengkap</label
            >
            <input
              v-model="formData.nama"
              type="text"
              class="w-full px-4 py-2.5 rounded-lg border border-gray-300 focus:ring-2 focus:ring-orange-500 outline-none"
              placeholder="John Doe"
            />
          </div>

          <div>
            <label class="block text-sm font-medium text-gray-700 mb-1"
              >Email</label
            >
            <input
              v-model="formData.email"
              type="email"
              class="w-full px-4 py-2.5 rounded-lg border border-gray-300 focus:ring-2 focus:ring-orange-500 outline-none"
              placeholder="nama@email.com"
            />
          </div>

          <div>
            <label class="block text-sm font-medium text-gray-700 mb-1"
              >Username</label
            >
            <input
              v-model="formData.username"
              type="text"
              class="w-full px-4 py-2.5 rounded-lg border border-gray-300 focus:ring-2 focus:ring-orange-500 outline-none"
              placeholder="johndoe123"
            />
          </div>

          <div>
            <label class="block text-sm font-medium text-gray-700 mb-1"
              >Password</label
            >
            <input
              v-model="formData.password"
              type="password"
              class="w-full px-4 py-2.5 rounded-lg border border-gray-300 focus:ring-2 focus:ring-orange-500 outline-none"
              placeholder="Minimal 6 karakter"
            />
          </div>

          <div
            v-if="error"
            class="p-3 rounded-lg bg-red-50 text-red-600 text-sm border border-red-200"
          >
            {{ error }}
          </div>
          <div
            v-if="success"
            class="p-3 rounded-lg bg-green-50 text-green-600 text-sm border border-green-200"
          >
            {{ success }}
          </div>

          <button
            type="submit"
            :disabled="loading"
            class="w-full bg-orange-600 hover:bg-orange-700 text-white font-bold py-3 rounded-lg shadow-md hover:shadow-lg transition-all disabled:opacity-70 flex justify-center"
          >
            <span
              v-if="loading"
              class="w-5 h-5 border-2 border-white border-t-transparent rounded-full animate-spin mr-2"
            ></span>
            {{ loading ? "Mendaftarkan..." : "Daftar Sekarang" }}
          </button>
        </form>

        <div class="mt-6 text-center text-sm text-gray-600">
          Sudah punya akun?
          <router-link
            to="/login"
            class="text-orange-600 font-bold hover:underline"
            >Login disini</router-link
          >
        </div>
      </div>
    </div>
  </div>
</template>
