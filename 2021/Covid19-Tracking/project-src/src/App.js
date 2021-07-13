import { useEffect, useState } from 'react'
import { getCountries, getReportByCountry } from "./apis";
import Country from "./components/Country";
import Highlight from "./components/Highlight";
import Summary from "./components/Summary";

function App() {

  const [countries, setCountries] = useState([]);
  const [selectedCountryID, setSelectedCountryID] = useState('');
  const [report, setReport] = useState([]);

  useEffect(() => {
    getCountries().then((res) => {
      console.log({ res });
      setCountries(res.data);
      setSelectedCountryID('vn');
    });
  } , []);

  const handleOnChange = (event) => {
    setSelectedCountryID(event.target.value);
  }

  useEffect(() => {
    if (selectedCountryID) {
      const { Slug } = countries.find(
        (country) => country.ISO2.toLowerCase() === selectedCountryID
      );
      getReportByCountry(Slug).then((res) => {
        console.log('getReportByCountry', { res });
        // remove last item = current date
        res.data.pop();
        setReport(res.data);
      });
    }
  }, [selectedCountryID, countries]);

  return (
    <>
      <Country countries={countries} handleOnChange={handleOnChange} value={selectedCountryID} />
      <Highlight report={report} />
      <Summary report={report} />
    </>
  );
}

export default App;
