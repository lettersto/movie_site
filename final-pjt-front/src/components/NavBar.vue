<template>
  <nav>
    <ul>
      <div>
        <li>
          <router-link :to="{ name: 'home' }">Home</router-link>
        </li>
        <li>
          <router-link :to="{ name: 'community' }">Community</router-link>
        </li>
      </div>
      
      <div>
        <search-bar />
      </div>

      <div>
        <li>
          <router-link :to="{ name: 'signup' }">Signup</router-link>
        </li>
        <li>
          <router-link :to="{ name: 'login' }">Login</router-link>
        </li>
        <li>
          <router-link :to="{ name: 'logout' }">Logout</router-link>
        </li>
        <li>
          <router-link :to="{ name: 'profile' }">Profile</router-link>
        </li>
      </div>
    </ul>
  </nav>
</template>

<script>
import SearchBar from './SearchBar.vue'

export default {
  name: 'NavBar',
  components: {
    SearchBar,
  }
}
</script>

<style>

</style>