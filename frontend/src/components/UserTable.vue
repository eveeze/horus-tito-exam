<script setup>
import { defineProps, defineEmits } from "vue";
import { useRouter } from "vue-router";

defineProps({
  users: {
    type: Array,
    required: true,
  },
});

const emit = defineEmits(["delete"]);
const router = useRouter();

const handleEdit = (userId) => {
  router.push(`/users/${userId}/edit`);
};

const handleDelete = (userId, username) => {
  if (confirm(`Apakah Anda yakin ingin menghapus user "${username}"?`)) {
    emit("delete", userId);
  }
};
</script>

<template>
  <div class="overflow-x-auto bg-white rounded-lg shadow">
    <table class="min-w-full table-auto border-collapse">
      <thead class="bg-orange-500 text-white">
        <tr>
          <th class="px-6 py-3 text-left text-sm font-semibold">ID</th>
          <th class="px-6 py-3 text-left text-sm font-semibold">Username</th>
          <th class="px-6 py-3 text-left text-sm font-semibold">
            Nama Lengkap
          </th>
          <th class="px-6 py-3 text-left text-sm font-semibold">Email</th>
          <th class="px-6 py-3 text-center text-sm font-semibold">Aksi</th>
        </tr>
      </thead>
      <tbody class="divide-y divide-gray-200">
        <tr v-for="user in users" :key="user.id" class="hover:bg-gray-50">
          <td class="px-6 py-4 text-sm text-gray-900">{{ user.id }}</td>
          <td class="px-6 py-4 text-sm text-gray-900">{{ user.username }}</td>
          <td class="px-6 py-4 text-sm text-gray-900">{{ user.nama }}</td>
          <td class="px-6 py-4 text-sm text-gray-900">{{ user.email }}</td>
          <td class="px-6 py-4 text-sm text-center">
            <button
              @click="handleEdit(user.id)"
              class="px-3 py-1 bg-blue-500 text-white rounded hover:bg-blue-600 mr-2"
            >
              Edit
            </button>
            <button
              @click="handleDelete(user.id, user.username)"
              class="px-3 py-1 bg-red-500 text-white rounded hover:bg-red-600"
            >
              Hapus
            </button>
          </td>
        </tr>
        <tr v-if="users.length === 0">
          <td colspan="5" class="px-6 py-8 text-center text-gray-500">
            Tidak ada data user
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>
