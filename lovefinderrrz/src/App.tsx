import { Route, Routes, useLocation } from "react-router-dom";
import { HeaderContainer } from "./componets/StyleContainer";
import { Home } from "./pages/Home";
import { Login } from "./pages/Login";
import { About } from "./pages/About";
import { Admin } from "./pages/Admin/Admin";
import { FindUsers } from "./pages/Admin/FindUsers";
import { EditUsers } from "./pages/Admin/EditUsers";
import { UserPage } from "./pages/User";
import { Navbar } from "./componets/NavBar";
import { Website } from "./pages/Website";
import { NewUser } from "./pages/NewUser";
import { UserProfile } from "./pages/UserProfile";

function App() {
  const isAdmin = sessionStorage.getItem("is_admin") === "true";
  const location = useLocation();
  const hideNavbar =
    location.pathname === "/" || location.pathname === "/NewUser";

  return (
    <>
      <HeaderContainer>
        <a href="">+1 884 667-3742</a>
      </HeaderContainer>
      {!hideNavbar && <Navbar isAdmin={isAdmin} />}

      <Routes>
        <Route path="/" element={<Website />} />
        <Route path="/Login" element={<Login />} />
        <Route path="/Home" element={<Home />} />
        <Route path="/About" element={<About />} />
        <Route path="/User" element={<UserPage />} />
        <Route path="/Admin" element={<Admin />} />
        <Route path="/FindUsers" element={<FindUsers />} />
        <Route path="/EditUsers" element={<EditUsers />} />
        <Route path="/NewUser" element={<NewUser />}></Route>
        <Route path="/UserProfile/:username" element={<UserProfile />}></Route>
      </Routes>
    </>
  );
}

export default App;
