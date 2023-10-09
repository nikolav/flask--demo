
import "bootstrap";
import $ from "jquery";

$(() => {
  const win$ = $(window);
  const nodes$ = $("body *");
  console.log({ nodes$, win$ });

  const btn$ = $("#b01");
  btn$.on({
    click: (evt) => {
      console.log({ evt });
    }
  })

});
