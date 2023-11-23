
<template>
    <div class="p-5">
        <h1>저축성 상품</h1>
        <ul class="nav nav-tabs">
            <li class="nav-item">

                <RouterLink :to="{ name: 'DepositView' }" class="nav-link active" aria-current="page" >예금</RouterLink>
            </li>
            <li class="nav-item">
                <RouterLink :to="{ name: 'SavingView' }" class="nav-link">적금</RouterLink>
            </li>
        </ul>
        <!-- 예금 -->
        <DepositList type="deposit" />        
    </div>
</template>

<script setup>
import { RouterLink } from 'vue-router'
import DepositList from "@/components/DepositList.vue"


</script>
<style scoped>
.nav-link {
  color: rgb(173, 173, 173);
}
</style>
