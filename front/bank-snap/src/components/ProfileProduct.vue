<template>
    <div class="card-body">
        <p class="card-text text-start">
            <RouterLink 
                v-for="product in products" 
                :key="product.id"
                :to="{ name: 'ProductDetailView', params: { id: product.id }}">
                <p>[{{ product.fin_prdt_cd }}] {{ product.kor_co_nm }} : {{ product.fin_prdt_nm }}</p>
            </RouterLink>
        </p>
    </div>
            
        
        
</template>

<script setup>
import { ref } from 'vue'
import { useIndexStore } from '@/stores/index'

const store = useIndexStore()

const props = defineProps({
    'products': Object,
})
const products = ref(props.products)
</script>
