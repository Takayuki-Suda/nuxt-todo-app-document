<template>
  <div>
    <h1>タスク一覧</h1>
    <ul>
      <li v-for="task in tasks" :key="task.id">
        {{ task.text }} - {{ task.dueDate }}
        <button @click="completeTask(task.id)">完了</button>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  data() {
    return {
      tasks: [],
    };
  },
  mounted() {
    this.fetchTasks();
  },
  methods: {
    fetchTasks() {
      // APIからタスクを取得する例
      axios.get("/api/tasks").then((response) => {
        this.tasks = response.data;
      });
    },
    completeTask(id) {
      // タスクを完了するAPI呼び出し例
      axios.post(`/api/tasks/${id}/complete`).then(() => {
        this.fetchTasks();
      });
    },
  },
};
</script>

<style scoped>
/* スタイルの例 */
button {
  margin-left: 10px;
}
</style>
