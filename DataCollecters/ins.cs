using System.IO;
using System.Net;

class InstNatStat {
	static public int Main() {
	WebRequest request = WebRequest.Create("http://dataportal.ins.tn/WebApi/GetData");
	request.Method = WebRequestMethods.Http.Post;
	string _request = @"<QueryMessage SourceId='C_NSO'>
<Period> </Period>
<DataWhere>
<Dimension Id='RDS_DICT_INDICATORS_NSO'>
<Element>11921416</Element>
</Dimension>
<Dimension Id='RDS_DICT_REGIONS_NSO'> </Dimension>
</DataWhere>
</QueryMessage>";
	byte[] bytes = System.Text.Encoding.UTF8.GetBytes(_request);
	request.ContentType = "text/xml; charset=UTF-8";
	request.ContentLength = bytes.Length;
	using(Stream dataStream = request.GetRequestStream()){
		dataStream.Write(bytes, 0, bytes.Length);
	}
	using(WebResponse response = request.GetResponse()){
		using(Stream stream = response.GetResponseStream()){
			StreamReader reader = new StreamReader(stream);
			string result = reader.ReadToEnd();
			}
	}
	return 0 ; 
	}
}
