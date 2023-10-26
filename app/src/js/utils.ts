const $ = (S: string) => document.querySelector(S);
const $$ = (S: string) => Array.from(document.querySelectorAll(S));

export { $, $$ };
