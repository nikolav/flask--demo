import axios from "axios";
import $ from "jquery";
import * as $$ from "bootstrap";

import { API_URL_DOCS } from "../config/vars";
import { subscribe, publish } from "./pubsub";

const TOPIC = "@1";

(async () => {
  // # https://api.jquery.com/jQuery.ready/
  await $.ready;

  // output
  const consolePre$ = $("#console");

  // init popovers
  const popoverAll$ = $('[data-bs-toggle="popover"]').map(
    (i, node) => new $$.Popover(node)
  );
  // init toasts
  const toastAll$ = $(".toast").map((i, node) => new $$.Toast(node));

  // init tooltips
  const tooltipAll$ = $('[data-bs-toggle="tooltip"]').map(
    (i, node) => new $$.Tooltip(node)
  );

  // collect/init bs-components
  const ui = {
    modal1: new $$.Modal("#modal_1"),
  };

  // const modal = new $$.Modal("#modal_1");
  $("#modal-1--open").on({
    click: () => ui.modal1.show(),
  });
  $(".modal-1--close").on({ click: () => ui.modal1.hide() });

  subscribe(({ type, payload }) => {
    switch (true) {
      // #
      case "@data:read" === type:
        consolePre$.text(JSON.stringify(payload, null, 2));
        ui.modal1.show();
        break;
      default:
        break;
    }
  });

  const btn$ = $("#B__ok");

  btn$.on({
    click: async (evt) => {
      const { data: payload } = await axios(
        `${API_URL_DOCS}?tag=${encodeURIComponent(TOPIC)}`
        // `${API_URL_DOCS}/23`
      );

      publish({
        type: "@data:read",
        payload,
      });
    },
  });
})();
