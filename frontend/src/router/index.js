import { createRouter, createWebHistory } from "vue-router";
import { useAuthStore } from "@/stores/auth";

const routes = [
  {
    path: "/",
    redirect: "/login",
  },
  {
    path: "/login",
    name: "Login",
    component: () => import("@/views/Login.vue"),
    meta: { requiresGuest: true },
  },
  {
    path: "/register",
    name: "Register",
    component: () => import("@/views/Register.vue"),
    meta: { requiresGuest: true },
  },
  {
    path: "/dashboard",
    name: "Dashboard",
    component: () => import("@/views/Dashboard.vue"),
    meta: { requiresAuth: true },
  },
  {
    path: "/users/:id/edit",
    name: "UpdateUser",
    component: () => import("@/views/UpdateUser.vue"),
    meta: { requiresAuth: true },
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

// Navigation Guard
router.beforeEach((to, from, next) => {
  const authStore = useAuthStore();

  if (to.meta.requiresAuth && !authStore.isAuthenticated) {
    next("/login");
  } else if (to.meta.requiresGuest && authStore.isAuthenticated) {
    next("/dashboard");
  } else {
    next();
  }
});

export default router;
