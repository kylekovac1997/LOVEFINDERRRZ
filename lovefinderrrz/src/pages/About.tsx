import styled from "styled-components";
import jerrypic from "../componets/images/jerrysmith.jpeg";
import glootiepic from "../componets/images/glootie.jpeg";
const UserContainer = styled.div`
  display: grid;
  grid-template-areas:
    "picture main main main"
    "details details details picture2"
    "footer footer footer footer";
  gap: 10px;
  background-color: #04b4b4;
  padding: 10px;
  align-items: center;
  margin-bottom: 20px;
`;

const Picture = styled.img`
  background-image: url(${jerrypic});
  background-repeat: no-repeat;
  background-size: cover;
  background-position: center;
  grid-area: picture;
  width: 350px;
  height: 200px;
`;
const Picture2 = styled.img`
  background-image: url(${glootiepic});
  background-repeat: no-repeat;
  background-size: cover;
  background-position: center;
  grid-area: picture2;
  width: 200px;
  height: 200px;
`;

const MainInfo = styled.div`
  grid-area: main;
`;

const Details = styled.div`
  grid-area: details;
`;

const FooterContainer = styled.footer`
  color: #fff;
  padding: 20px;
  text-align: center;
`;
export const About = () => {
  return (
    <>
      <UserContainer>
        <MainInfo>
          <p>
            Welcome to LoveFinderrrz, the groundbreaking dating website created
            by Jerry Smith and Glootie! With their shared passion for technology
            and a catchphrase that echoes, "Would you like to develop an app?",
            they have revolutionized the way people connect and find love in the
            digital age.
          </p>
        </MainInfo>
        <Details>
          <p>
            Jerry Smith, an ambitious entrepreneur with a knack for coding,
            joined forces with Glootie, a brilliant and quirky software
            engineer. Together, they set out on a mission to create an
            innovative platform that would transcend traditional dating norms
            and embrace the ever-evolving world of technology.
          </p>
          <p>
            LoveFinderrrz is more than just a dating website. It's an immersive
            experience where users can discover a universe of potential matches
            while indulging in their shared love for app development. The
            platform brings together individuals from all walks of life who
            appreciate the thrill of building and creating something
            extraordinary.
          </p>
          <p>
            Jerry and Glootie believe that true love can be found through shared
            passions and a common vision. They have meticulously designed
            LoveFinderrrz to foster meaningful connections based on mutual
            interests, compatible coding languages, and a shared enthusiasm for
            technological advancement.
          </p>
          <p>
            Upon joining LoveFinderrrz, users are encouraged to showcase their
            app development skills, share their project ideas, and connect with
            fellow tech enthusiasts. The platform provides a vibrant community
            where individuals can engage in stimulating conversations,
            collaborate on exciting projects, and even embark on thrilling
            coding adventures together.
          </p>
          <p>
            Jerry and Glootie's catchphrase, "Would you like to develop an
            app?", encapsulates their belief that love can flourish when shared
            ambitions align. It's an invitation to explore not only romantic
            connections but also the exhilarating world of technology and
            innovation.
          </p>
          <p>
            So, whether you're an aspiring developer seeking a coding companion
            or a tech enthusiast looking for a love interest who shares your
            passion, LoveFinderrrz is the perfect place for you. Join us today
            and let the sparks of love and app development ignite a remarkable
            journey of connection, collaboration, and endless possibilities.
          </p>
        </Details>
        <Picture></Picture>
        <Picture2></Picture2>
        <FooterContainer>
          <p>&copy; 2023 LoveFinderrrz. All rights reserved.</p>
        </FooterContainer>
      </UserContainer>
    </>
  );
};
