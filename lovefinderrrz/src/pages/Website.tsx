import { Registration } from "../componets/RegisterForm";
import Login from "./Login";

export const Website = () => {
  return (
    <div>
      this the the front website
      <div>
        <Login />
      </div>
      <div style={{ right: "20px" }}>
        <Registration />
      </div>
    </div>
  );
};
