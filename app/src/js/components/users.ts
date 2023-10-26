import rand from "lodash/random";

export default () => ({
  active: "",
  hovered: "",
  ls: [],

  async init() {
    console.log({ "User:self": this });
  },
  setActive(u = "") {
    this.active = u;
  },
  setHovered(u = "") {
    this.hovered = u;
  },
  userAddRand() {
    const u = `user:${rand(9999)}`;
    this.ls.push(u);
  },
  usersRm(uname) {
    this.ls = this.ls.filter((name) => uname !== name);
  },
  get isNotEmpty() {
    return !this.isEmpty;
  },
  get isEmpty() {
    return 0 === this.ls.length;
  },
});
