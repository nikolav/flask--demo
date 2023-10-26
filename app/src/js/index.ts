import alpine from "alpinejs";
import * as $$$ from "bootstrap";

import { Users } from "./components";
import { Main } from "./store";

import { subscribe } from "./pubsub";
import { $$ } from "./utils";

(async () => {
  // init popovers
  const popoverAll$ = $$('[data-bs-toggle="popover"]').map(
    (node) => new $$$.Popover(node)
  );

  // init toasts
  const toastAll$ = $$(".toast").map((node) => new $$$.Toast(node));

  // init tooltips
  const tooltipAll$ = $$('[data-bs-toggle="tooltip"]').map(
    (node) => new $$$.Tooltip(node)
  );

  // @components.alpine
  alpine.store("main", Main);
  alpine.data("users", Users);

  subscribe(({ type, payload }) => {
    console.log({ [type]: payload });
  });

  alpine.start();
})();
