<script setup>
import { ref, onMounted, computed } from "vue";
import { useRouter } from "vue-router";
import { useAuthStore } from "@/stores/auth";
import api from "@/services/api";
import UserTable from "@/components/UserTable.vue";
import SearchBar from "@/components/SearchBar.vue";

const router = useRouter();
const authStore = useAuthStore();

const users = ref([]);
const searchQuery = ref("");
const loading = ref(false);
const error = ref("");

const filteredUsers = computed(() => {
  if (!searchQuery.value) return users.value;

  const query = searchQuery.value.toLowerCase();
  return users.value.filter(
    (user) =>
      user.nama.toLowerCase().includes(query) ||
      user.username.toLowerCase().includes(query) ||
      user.email.toLowerCase().includes(query)
  );
});

const fetchUsers = async () => {
  loading.value = true;
  error.value = "";

  try {
    const response = await api.get("/users");
    users.value = response.data;
  } catch (err) {
    error.value = err.response?.data?.error || "Gagal memuat data user";
  } finally {
    loading.value = false;
  }
};

const handleDelete = async (userId) => {
  try {
    await api.delete(`/users/${userId}`);
    await fetchUsers();
  } catch (err) {
    alert(err.response?.data?.error || "Gagal menghapus user");
  }
};

const handleLogout = () => {
  if (confirm("Apakah Anda yakin ingin logout?")) {
    authStore.logout();
    router.push("/login");
  }
};

onMounted(() => {
  fetchUsers();
});
</script>

<template>
  <div class="min-h-screen bg-gray-50">
    <!-- Navbar -->
    <nav class="bg-orange-500 text-white shadow-lg">
      <div
        class="container mx-auto px-4 py-4 flex items-center justify-between"
      >
        <div>
          <h1 class="text-2xl font-bold">User Management Dashboard</h1>
          <p class="text-orange-100 text-sm">Horus Theme</p>
        </div>
        <button
          @click="handleLogout"
          class="bg-white text-orange-600 px-6 py-2 rounded-lg hover:bg-orange-50 font-semibold"
        >
          Logout
        </button>
      </div>
    </nav>

    <!-- Main Content -->
    <div class="container mx-auto px-4 py-8">
      <!-- Header & Search -->
      <div
        class="mb-6 flex flex-col md:flex-row items-start md:items-center justify-between gap-4"
      >
        <div>
          <h2 class="text-2xl font-bold text-gray-800">Daftar User</h2>
          <p class="text-gray-600 mt-1">Total: {{ users.length }} user</p>
        </div>
        <SearchBar v-model="searchQuery" />
      </div>

      <!-- Error Message -->
      <div
        v-if="error"
        class="mb-6 p-4 bg-red-100 border border-red-400 text-red-700 rounded-lg"
      >
        {{ error }}
      </div>

      <!-- Loading State -->
      <div v-if="loading" class="text-center py-12">
        <div
          class="inline-block h-8 w-8 animate-spin rounded-full border-4 border-solid border-orange-500 border-r-transparent"
        ></div>
        <p class="mt-4 text-gray-600">Memuat data...</p>
      </div>

      <!-- User Table -->
      <UserTable v-else :users="filteredUsers" @delete="handleDelete" />

      <!-- No Results -->
      <div
        v-if="!loading && filteredUsers.length === 0 && searchQuery"
        class="text-center py-12"
      >
        <p class="text-gray-600">
          Tidak ada hasil untuk pencarian "{{ searchQuery }}"
        </p>
      </div>
    </div>
  </div>
</template>
