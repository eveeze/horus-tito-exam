import { defineStore } from "pinia";
import { ref, computed } from "vue";
import api from "@/services/api";

export const useAuthStore = defineStore("auth", () => {
  const token = ref(localStorage.getItem("token") || null);
  const user = ref(null);

  const isAuthenticated = computed(() => !!token.value);

  const login = async (username, password) => {
    try {
      const response = await api.post("/users/login", { username, password });
      token.value = response.data.token;
      localStorage.setItem("token", response.data.token);
      return { success: true, message: response.data.message };
    } catch (error) {
      return {
        success: false,
        message: error.response?.data?.error || "Login gagal",
      };
    }
  };

  const logout = () => {
    token.value = null;
    user.value = null;
    localStorage.removeItem("token");
  };

  return {
    token,
    user,
    isAuthenticated,
    login,
    logout,
  };
});
