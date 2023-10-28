import axios from "axios";
// #https://vanilla-swr.js.org/#/?id=vanilla-swr
import SWR from "vanilla-swr";
import get from "lodash/get";
import assign from "lodash/assign";
import { idGen } from "nikolav-utils";

export default {
  //
  swr$: null,
  watcher$: null,
  //
  a: -1,
  data: {},

  async init() {
    const main$ = this;
    const swr = SWR(
      // key
      "/api/data --read",
      // fetcher
      async (key) =>
        get(await axios("http://127.0.0.1:8000/docs?tag=app:config:2"), "data"),
      // options
      {
        refreshInterval: 23456,
      }
    );
    //
    main$.watcher$ = swr.watch(({ data, error }) => assign(main$.data, data));
    main$.swr$ = swr;
  },

  logData() {
    const data = this.data;
    console.clear();
    console.log({ data });
  },

  get sData() {
    return JSON.stringify(this.data, null, 2);
  },

  async updateData() {
    const main$ = this;
    let res = null;
    try {
      res = await axios({
        method: "post",
        url: "http://127.0.0.1:8000/docs",
        data: {
          tag: "app:config:2",
          data: JSON.stringify({ "app:key": idGen() }),
          id: 26,
        },
      });
    } finally {
      if (get(res, "data.id")) main$.swr$.mutate();
    }
  },

  aIncrement() {
    this.a += 1;
  },
};
