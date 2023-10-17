import EE from "eventemitter3";

interface IPubSubEvent<TPayload = any> {
  type: string;
  payload?: TPayload;
}
const EVENT__PUBSUB = "Lczl6c2QrdT";

const emitter = new EE();

const publish = (event: IPubSubEvent): void => {
  emitter.emit(EVENT__PUBSUB, event);
};
const subscribe = (callback: (event: IPubSubEvent) => void): void => {
  emitter.on(EVENT__PUBSUB, callback);
};

export { publish, subscribe, emitter, EVENT__PUBSUB, IPubSubEvent };
