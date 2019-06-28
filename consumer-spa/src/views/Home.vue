<template>
  <div class="layout-margin">
    <div class="layout-row layout-align-space-between-start flex">
      <photo class="flex-30 hide-xs" :image="require('@/assets/icons/customers.svg')"></photo>
      <div class="layout-column flex">
        <div class="layout-row layout-margin layout-align-end-center">
          <button
            class="button-primary"
            type="button"
            @click.stop.prevent="createConsumer()"
          >Create Customer</button>
        </div>
        <div class="flex layout-row layout-align-center" v-if="consumers.length == 0">No registered clients</div>
        <div class="layout-row layout-wrap layout-margin">
          <div
            v-for="consumer in consumers"
            v-bind:key="consumer.id"            
            class="flex-gt-xs-33 flex-100 md-list-item md-2-line contact-item"
          >
            <photo
              class="md-avatar"
              :image="`https://placeimg.com/128/128/people/${consumer.id}`"
            ></photo>
            <div class="md-list-item-text compact">
              <a href="" @click.stop.prevent="removeConsumer(consumer.id)"><h3>{{consumer.name}}</h3></a>
              <p>{{consumer.address}}</p>
            </div>
            <div class="md-secondary-container"></div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src

import Photo from "@/components/Photo";
import Axios from "axios";
import Leite from "leite";

export default {
  name: "home",
  components: {
    Photo
  },
  data() {
    return {
      consumers: []
    };
  },
  methods: {
    async getConsumers() {
      try {
        const { data: consumers } = await Axios.get(
          `${process.env.VUE_APP_ROOT_API}/consumer/`
        );

        this.consumers = consumers;

      } catch (error) {
        console.error(error);
      }
    },
    async createConsumer() {
      const leite = new Leite();
      const consumer = {
        name: leite.pessoa.nome(),
        address: leite.localizacao.logradouro(),
        age: this.getAge(leite.pessoa.nascimento())
      };
      await Axios.post(`${process.env.VUE_APP_ROOT_API}/consumer/`, consumer);
      await this.getConsumers();
    },
    getAge(birthDate) {
      const today = new Date();
      let age = today.getFullYear() - birthDate.getFullYear();
      const m = today.getMonth() - birthDate.getMonth();
      if (m < 0 || (m === 0 && today.getDate() < birthDate.getDate())) {
        age = age - 1;
      }

      return age;
    },
    async removeConsumer(id) {
      await Axios.delete(`${process.env.VUE_APP_ROOT_API}/consumer/${id}/`);
      await this.getConsumers();
    }
  },
  async created() {
    await this.getConsumers();
  }
};
</script>

<style lang="scss">
.md-list-item.md-2-line {
  float: left;
  box-sizing: border-box;
  height: auto;
  min-height: 72px;
  align-items: flex-start;
  justify-content: center;
  position: relative;
  padding: 0 16px;
  flex: 1 1 auto;
  display: flex;
}

.md-list-item.md-2-line > .md-avatar {
  margin-top: 12px;
  flex: none;
  width: 40px;
  height: 40px;
  margin-bottom: 8px;
  margin-right: 16px;
  border-radius: 50%;
  box-sizing: content-box;
}

.md-list-item.md-2-line .md-list-item-text {
  flex: 1 1 auto;
  margin: auto;
  text-overflow: ellipsis;
  overflow: hidden;
  padding: 14px 0;
  max-width: 190px;
}
.contact-item .md-list-item-text a {
  color: #000;
  text-decoration: none;
}
.contact-item .md-list-item-text h3 {
  margin: 0 !important;
  padding: 0;
  line-height: 1.2em !important;
  text-overflow: ellipsis;
  white-space: nowrap;
  overflow: hidden;
  font-size: 16px;
  font-weight: bold;
  letter-spacing: 0.01em;
  display: block;
}

.md-list-item.md-2-line .md-list-item-text p {
  font-size: 14px;
  font-weight: 500;
  letter-spacing: 0.01em;
  margin: 0;
  line-height: 1.6em;
  color: rgba(0, 0, 0, 0.54);
  text-overflow: ellipsis;
  white-space: nowrap;
  overflow: hidden;
}

.md-list-item .md-secondary-container {
  display: flex;
  align-items: center;
  position: relative;
  flex-shrink: 0;
  margin: auto;
  margin-right: 0;
  margin-left: auto;
}

button.button-primary {
  box-shadow: 0 2px 5px 0 rgba(0, 0, 0, 0.26);
  color: rgba(255, 255, 255, 0.87);
  background-color: rgb(0, 78, 116);
  border-radius: 16px;
  padding: 0 16px;
  transition-duration: 0.5s;
  transition-timing-function: cubic-bezier(0.35, 0, 0.25, 1);
  transition-property: background-color, fill, color;
  margin-top: 0;
  margin-bottom: 0;
  max-width: 100%;
  box-sizing: border-box;
  display: inline-block;
  position: relative;
  cursor: pointer;
  min-height: 36px;
  min-width: 88px;
  line-height: 36px;
  vertical-align: middle;
  align-items: center;
  text-align: center;
  user-select: none;
  outline: 0;
  border: 0;
  margin: 6px 8px;
  white-space: nowrap;
  text-transform: uppercase;
  font-weight: 500;
  font-size: 14px;
  font-style: inherit;
  font-variant: inherit;
  font-family: inherit;
  text-decoration: none;
  overflow: hidden;
  transition: box-shadow 0.4s cubic-bezier(0.25, 0.8, 0.25, 1),
    background-color 0.4s cubic-bezier(0.25, 0.8, 0.25, 1);
}

button.button-primary:hover {
  background-color: rgb(0, 71, 108);
}
button.button-primary:active {
  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.4);
}
</style>