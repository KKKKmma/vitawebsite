import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue';
import Helper from '../views/Helper.vue';
import NProgress from 'nprogress';
import Productcatalogue from '../components/Product/Product-catalogue.vue';
import Productinfo from '../components/Product/Product-info.vue';
import Rent from '../components/Rent.vue';
import News from '../components/News.vue';
import Booking from '../components/Booking.vue';
import Bookinglist from '../components/Booking-list.vue';
import Cart from '../components/Cart.vue';
import Creative from '../components/Creative.vue';
import Course from '../components/Course.vue';
import Demo from '../components/Demo.vue';
const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/help',
    name: 'Help',
    component: Helper
  },
  {
    path: '/Demo',
    name: 'Demo',
    component: Demo
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  },
  {
    path: '/Product-catalogue',
    name: 'Product-catalogue',
    component: Productcatalogue
  },
  {
    path: '/Product-info',
    name: 'Productinfo',
    component: Productinfo
  },
  {
    path: '/rent',
    name: 'rent',
    component: Rent
  },
  {
    path: '/news',
    name: 'News',
    component: News
  },
  {
    path: '/cart',
    name: 'Cart',
    component: Cart
  },
  {
    path: '/creative',
    name: 'Creative',
    component: Creative
  },
  {
    path: '/course',
    name: 'Course',
    component: Course
  },
  {
    path: '/Booking',
    name: 'Booking',
    component: Booking
  },
  {
    path: '/Bookinglist',
    name: 'Bookinglist',
    component: Bookinglist
  },
  {
    path: '/products',
    name: 'Products',
    component: () => import('../views/products/ProductList.vue')
  },
  {
    path: '/products/create',
    name: 'Product Create',
    component: () => import('../views/products/ProductCreate.vue')
  },
  {
    path: '/products/edit/:id',
    name: 'ProductEdit',
    component: () => import('../views/products/ProductEdit.vue')
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

router.beforeResolve((to, from, next) => {
  if (to.name) {
      NProgress.start()
  }
  next()
});

router.afterEach(() => {
  NProgress.done()
});

export default router
