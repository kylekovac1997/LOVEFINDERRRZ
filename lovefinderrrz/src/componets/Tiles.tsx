interface AdoptionTilesProps {
  image: string;
  text: string;
  text1: string;
  text2: string;
}

const AdoptionTiles: React.FC<AdoptionTilesProps> = ({
  image,
  text,
  text1,
  text2,
}) => {
  return (
    <div id="adoptionsTiles" className="card" style={{ width: "17rem" }}>
      <img src={image} className="card-img-top" alt="adoption-card" />
      <div className="card-body">
        <p className="card-text">{text}</p>
        <p className="card-text">{text1}</p>
        <p className="card-text">{text2}</p>
      </div>
    </div>
  );
};

export default AdoptionTiles;
