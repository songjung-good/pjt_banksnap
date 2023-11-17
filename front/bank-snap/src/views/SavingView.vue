
<template>
    <div>
        <h1>Interest-Rates</h1>
        <!-- 적금 -->
        <div>
            <RouterLink :to="{ name: 'DepositView' }">예금</RouterLink> | 
            <RouterLink :to="{ name: 'SavingView' }">적금</RouterLink>
        </div>
        <DepositList type="saving" />        
    </div>
</template>

<script setup>
import DepositList from "@/components/DepositList.vue"


</script>
<style scoped>

</style>
