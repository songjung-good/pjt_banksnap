<template>
    <div>
        <h3>관심 상품</h3>
        <RouterLink 
            v-for="product in products" 
            :key="product.id"
            :to="{ name: 'ProductDetailView', params: { id: product.id }}">
            <p>[{{ product.fin_prdt_cd }}] {{ product.kor_co_nm }} : {{ product.fin_prdt_nm }}</p>
        </RouterLink>
        
    </div>
</template>

<script setup>
import { ref } from 'vue'
import { useCounterStore } from '@/stores/counter'

const store = useCounterStore()

const props = defineProps({
    'products': Object,
})
const products = ref(props.products)
</script>
