<template>
  <div>
    <h3>댓글</h3>
    <CommentListItem  
      v-for="comment in comments"
      :key="comment.id"
      :comment="comment"
    />
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useIndexStore } from '@/stores/index'
import CommentListItem from '@/components/CommentListItem.vue'
import axios from 'axios'

const comments = ref(null)
const store = useIndexStore()
const props = defineProps({
  articleId: String,
})
onMounted(() => {
  axios({
      method: 'get',
      url: `${store.url}/articles/comments/${props.articleId}`,
      headers: {
        Authorization: `Token ${store.token}`
      }
    })
      .then((res) =>{
        comments.value = res.data
      })
      .catch((err) => {
        console.log(err)
      })
})

</script>
