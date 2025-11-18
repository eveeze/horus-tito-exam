<script setup>
import { defineProps, defineEmits } from "vue";

defineProps({
  modelValue: {
    type: String,
    default: "",
  },
});

const emit = defineEmits(["update:modelValue"]);

const handleInput = (event) => {
  emit("update:modelValue", event.target.value);
};
</script>

<template>
  <div class="w-full max-w-md">
    <input
      type="text"
      :value="modelValue"
      @input="handleInput"
      placeholder="Cari user (nama, username, email)..."
      class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-orange-500 focus:border-transparent"
    />
  </div>
</template>
