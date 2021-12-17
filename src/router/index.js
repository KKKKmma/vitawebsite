import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue';
import Helper from '../views/Helper.vue';
import NProgress from 'nprogress';
import productcatalogue from '../components/Product/productcatalogue.vue';
import Productinfo from '../components/Product/productinfo.vue';
import Rent from '../components/Rent.vue';
import News from '../components/News.vue';
import Booking from '../components/booking.vue';
import Bookinglist from '../components/bookinglist.vue';
import Bookingcheck from '../components/bookingcheck.vue';
import Cart from '../components/Cart.vue';
import Creative from '../components/Creative.vue';
import Course from '../components/Course.vue';
import Demo from '../components/Demo.vue';
import childrenproduct from '../components/children_product.vue';

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
    path: '/productcatalogue',
    name: 'productcatalogue',
    component: productcatalogue,
       children: [
       {
          path: '/',
          name: '/',
          components: {
            childrenlist: childrenproduct,
          },
          meta: { requiresAuth: false },
        },
        {
          path: 'men_clothing',
          name: 'men_clothing',
          components: {
            childrenlist: childrenproduct,
          },
          meta: { requiresAuth: false },
        },
        {
          path: 'women_clothing',
          name: 'women_clothing',
          components: {
            childrenlist: childrenproduct,
          },
          meta: { requiresAuth: false },
        },
        {
          path: 'kid_clothing',
          name: 'kid_clothing',
          components: {
            childrenlist: childrenproduct,
          },
          meta: { requiresAuth: false },
        },
        {
          path: 'accessories_clothing',
          name: 'accessories_clothing',
          components: {
            childrenlist: childrenproduct,
          },
          meta: { requiresAuth: false },
        }
        ]
  },
  {
    path: '/Productinfo',
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
    path: '/bookinglist',
    name: 'Bookinglist',
    component: Bookinglist
  },
  {
    path: '/bookingcheck',
    name: 'Bookinglist',
    component: Bookingcheck
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
