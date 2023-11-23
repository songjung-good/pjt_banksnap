<template>
  <div class="text-center p-5">
    <img class="mb-4" src="../assets/logo_nonbackgroound.png" alt="" width="80" height="57">
    <ul class="nav nav-tabs">
        <li class="nav-item">

            <p class="nav-link active" aria-current="page" >프로필</p>
        </li>
        <li class="nav-item">
            <RouterLink :to="{ name: 'PropensityView' }" class="nav-link">내 금융정보</RouterLink>
        </li>
    </ul>
    <h1 class="p-5">{{ username }} 님의 프로필</h1>
      <div class="card-group">
        <div class="card">
          <div class="card-header text-center">
                <h5>작성 게시글</h5>
            </div>
          <template v-if="articles.length > 0">
            <ProfileArticle :articles="articles" />
          </template>
          <template v-else>
            <div class="card-body">
              <p>작성 게시글이 없습니다.</p>
            </div>
          </template>
        </div>
        <div class="card">
          <div class="card-header text-center">
                <h5>작성 댓글</h5>
            </div>
          <template v-if="comments.length > 0">
            <ProfileComment :comments="comments" />
          </template>
          <template v-else>
            <div class="card-body">
              <p>작성 댓글이 없습니다.</p>
            </div>
          </template>
        </div>
        <div class="card">
          <div class="card-header text-center">
                <h5>관심 상품</h5>
            </div>
          <template v-if="products.length > 0">
            <ProfileProduct :products="products" />
          </template>
          <template v-else>
            <div class="card-body">
              <p>관심 상품이 없습니다.</p>
            </div>
          </template>
        </div>
      </div>
    </div>
    
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute, RouterLink } from 'vue-router'
import { useIndexStore } from '@/stores/index'
import axios from 'axios'

import ProfileArticle from '@/components/ProfileArticle.vue'
import ProfileComment from '@/components/ProfileComment.vue'
import ProfileProduct from '@/components/ProfileProduct.vue'

const store = useIndexStore()
const route = useRoute()

const username = ref('')
const articles = ref([])
const comments = ref([])
const products = ref([])

onMounted(() => {
  axios({
      method: 'get',
      url: `${store.url}/user/profile/${route.params.id}`,
      headers: {
        Authorization: `Token ${store.token}`
      }
    })
      .then((res) =>{
        username.value = res.data.username
        articles.value = res.data.article_set
        comments.value = res.data.comment_set
        products.value = res.data.like_products
      })
      .catch((err) => {
        console.log(err)
      })
})

</script>

<style>
a {
  color: black;
}
.nav-link {
  color: rgb(173, 173, 173);
}
</style>