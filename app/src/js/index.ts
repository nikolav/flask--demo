import $ from "jquery";
import "bootstrap";
import axios from "axios";


$(() => {
  console.log(`@ready [${Date.now()}]`);

  const btn$ = $("#B__ok");


  btn$.on({
    click: async (evt) => {
      const { data } = await axios({
        method: "get",
        url: "https://jsonplaceholder.typicode.com/posts/22",
      });
      alert(JSON.stringify(data));
    },
  });
});
