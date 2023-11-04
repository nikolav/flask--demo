import axios from "axios";
// #https://vanilla-swr.js.org/#/?id=vanilla-swr
import SWR from "vanilla-swr";
import get from "lodash/get";

import { idGen } from "nikolav-utils";

const TAG = "app:config";
const KEY__APP_CONFIG__LIST = "app:config@api.docs --list";

export default {
  //
  swr$: {
    main: {
      isValidating: null,
      client: null,
      watcher: null,
      data: {},
    },
  },
  //
  a: -1,

  async init() {
    const store$ = this;
    const clientMain = SWR(
      // key
      KEY__APP_CONFIG__LIST,
      // fetcher
      async (key) =>
        get(
          await axios(
            `http://127.0.0.1:8000/docs?tag=${encodeURIComponent(TAG)}`
          ),
          "data"
        ),
      // options
      {
        refreshInterval: 23456,
      }
    );
    //
    store$.swr$.main.watcher = clientMain.watch(
      ({ data, error, isValidating }) => {
        store$.swr$.main.isValidating = isValidating;
        if (!error) store$.swr$.main.data = data;
      }
    );
    store$.swr$.main.client = clientMain;
  },

  destroy() {
    const store$ = this;
    store$.swr$.main.watcher.unwatch();
  },

  logData() {
    const { data } = this.swr$.main;
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
          tag: TAG,
          data: JSON.stringify({
            "app:key": idGen(),
          }),
          id: 122,
        },
      });
    } finally {
      if (get(res, "data.id")) store$.swr$.main.client.mutate();
    }
  },
};
