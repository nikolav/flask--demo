export default {
  a: -1,

  async init() {
    this.a = await Promise.resolve(1);
    console.log({ a: this.a });
  },

  aIncrement() {
    this.a += 1;
  },
};
