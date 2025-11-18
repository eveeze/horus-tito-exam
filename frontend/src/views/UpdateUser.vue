<script setup>
import { ref, onMounted } from "vue";
import { useRouter, useRoute } from "vue-router";
import api from "@/services/api";

const router = useRouter();
const route = useRoute();

const userId = route.params.id;

const formData = ref({
  nama: "",
  email: "",
  username: "",
});

const error = ref("");
const success = ref("");
const loading = ref(false);
const loadingData = ref(true);

const validateEmail = (email) => {
  const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return regex.test(email);
};

const fetchUser = async () => {
  loadingData.value = true;
  try {
    const response = await api.get("/users");
    const user = response.data.find((u) => u.id === parseInt(userId));

    if (user) {
      formData.value = {
        nama: user.nama,
        email: user.email,
        username: user.username,
      };
    } else {
      error.value = "User tidak ditemukan";
    }
  } catch (err) {
    error.value = err.response?.data?.error || "Gagal memuat data user";
  } finally {
    loadingData.value = false;
  }
};

const handleUpdate = async () => {
  error.value = "";
  success.value = "";

  // Validasi
  if (
    !formData.value.nama ||
    !formData.value.email ||
    !formData.value.username
  ) {
    error.value = "Semua field harus diisi";
    return;
  }

  if (!validateEmail(formData.value.email)) {
    error.value = "Format email tidak valid";
    return;
  }

  loading.value = true;

  try {
    const response = await api.put(`/users/${userId}`, formData.value);
    success.value = response.data.message;

    setTimeout(() => {
      router.push("/dashboard");
    }, 1500);
  } catch (err) {
    error.value = err.response?.data?.error || "Gagal memperbarui user";
  } finally {
    loading.value = false;
  }
};

const handleBack = () => {
  router.push("/dashboard");
};

onMounted(() => {
  fetchUser();
});
</script>

<template>
  <div class="min-h-screen bg-gray-50">
    <!-- Navbar -->
    <nav class="bg-orange-500 text-white shadow-lg">
      <div class="container mx-auto px-4 py-4">
        <h1 class="text-2xl font-bold">Edit User</h1>
        <p class="text-orange-100 text-sm">Horus Theme</p>
      </div>
    </nav>

    <!-- Main Content -->
    <div class="container mx-auto px-4 py-8">
      <div class="max-w-2xl mx-auto">
        <!-- Loading State -->
        <div
          v-if="loadingData"
          class="bg-white rounded-lg shadow-lg p-8 text-center"
        >
          <div
            class="inline-block h-8 w-8 animate-spin rounded-full border-4 border-solid border-orange-500 border-r-transparent"
          ></div>
          <p class="mt-4 text-gray-600">Memuat data user...</p>
        </div>

        <!-- Form -->
        <div v-else class="bg-white rounded-lg shadow-lg p-8">
          <h2 class="text-2xl font-bold text-gray-800 mb-6">Edit Data User</h2>

          <form @submit.prevent="handleUpdate" class="space-y-5">
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
                placeholder="Nama lengkap"
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
                placeholder="Username"
              />
            </div>

            <div
              v-if="error"
              class="p-4 bg-red-100 border border-red-400 text-red-700 rounded-lg text-sm"
            >
              {{ error }}
            </div>

            <div
              v-if="success"
              class="p-4 bg-green-100 border border-green-400 text-green-700 rounded-lg text-sm"
            >
              {{ success }}
            </div>

            <div class="flex gap-4 pt-4">
              <button
                type="submit"
                :disabled="loading"
                class="flex-1 bg-orange-500 text-white py-2 px-4 rounded-lg hover:bg-orange-600 focus:outline-none focus:ring-2 focus:ring-orange-500 focus:ring-offset-2 disabled:opacity-50 disabled:cursor-not-allowed font-semibold"
              >
                {{ loading ? "Menyimpan..." : "Simpan Perubahan" }}
              </button>

              <button
                type="button"
                @click="handleBack"
                class="flex-1 bg-gray-500 text-white py-2 px-4 rounded-lg hover:bg-gray-600 focus:outline-none focus:ring-2 focus:ring-gray-500 focus:ring-offset-2 font-semibold"
              >
                Kembali
              </button>
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>
