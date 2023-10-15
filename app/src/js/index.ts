import axios from "axios";
import $ from "jquery";
import * as $$ from "bootstrap";

import { API_URL_DOCS } from "../config/vars";

const TOPIC = "@1";

$(() => {
  console.log(`@ready [${Date.now()}]`);
  console.log({ $$ });

  const btn$ = $("#B__ok");

  btn$.on({
    click: async (evt) => {
      const { data } = await axios(
        `${API_URL_DOCS}?tag=${encodeURIComponent(TOPIC)}`
        // `${API_URL_DOCS}/23`
      );

      alert(JSON.stringify(data));
    },
  });
});
