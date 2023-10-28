import axios from "axios";
// #https://vanilla-swr.js.org/#/?id=vanilla-swr
import SWR from "vanilla-swr";
import get from "lodash/get";
import { idGen } from "nikolav-utils";

export default {
  //
  swr$: {
    main: {
      client: null,
      watcher: null,
      data: null,
    },
  },
  //
  a: -1,

  async init() {
    const store$ = this;
    const swrMain = SWR(
      // key
      "/api/data/main --read",
      // fetcher
      async (key) =>
        get(await axios("http://127.0.0.1:8000/docs?tag=app:config:2"), "data"),
      // options
      {
        refreshInterval: 23456,
      }
    );
    //
    store$.swr$.main.watcher = swrMain.watch(({ data }) => {
      store$.swr$.main.data = data;
    });
    store$.swr$.main.client = swrMain;
  },

  logData() {
    const data = this.swr$.main.data;
    console.clear();
    console.log({ data });
  },

  get sData() {
    return JSON.stringify(this.swr$.main.data, null, 2);
  },

  async updateData() {
    const store$ = this;
    let res = null;
    try {
      res = await axios({
        method: "post",
        url: "http://127.0.0.1:8000/docs",
        data: {
          tag: "app:config:2",
          data: JSON.stringify({
            "app:password": idGen(),
          }),
          id: 5432,
        },
      });
    } finally {
      if (get(res, "data.id")) store$.swr$.main.client.mutate();
    }
  },

  aIncrement() {
    this.a += 1;
  },
};
