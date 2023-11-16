
<template>
    <div>
        <h1>Community</h1>
        <ArticleList />
    </div>
    <div>
        <b-button-toolbar key-nav aria-label="Toolbar with button groups">
            <b-button-group class="mx-1">
            <b-button>&laquo;</b-button>
            <b-button>&lsaquo;</b-button>
            </b-button-group>
            <b-button-group class="mx-1">
            <b-button><RouterLink :to="{ name: 'CreateArticleView', query:{ type: 'create' }}">글 쓰기</RouterLink></b-button>
            <b-button>Undo</b-button>
            <b-button>Redo</b-button>
            </b-button-group>
            <b-button-group class="mx-1">
            <b-button>&rsaquo;</b-button>
            <b-button>&raquo;</b-button>
            </b-button-group>
        </b-button-toolbar>
    </div>
</template>

<script setup>
import { onMounted } from 'vue'
import { useCounterStore } from '@/stores/counter'
import { RouterLink } from 'vue-router'
import ArticleList from '@/components/ArticleList.vue'

const store = useCounterStore()

onMounted(() => {
    store.getArticles()
})
</script>

<style scoped>

</style>
