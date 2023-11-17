
<template>
    <div>
        <h1>Interest-Rates</h1>
        <div>
            <RouterLink :to="{ name: 'DepositView' }">예금</RouterLink> | 
            <RouterLink :to="{ name: 'SavingView' }">적금</RouterLink>
        </div>
        <!-- 예금 -->
        <DepositList type="deposit" />        
    </div>
</template>

<script setup>
import { RouterLink } from 'vue-router'
import DepositList from "@/components/DepositList.vue"


</script>
<style scoped>

</style>
