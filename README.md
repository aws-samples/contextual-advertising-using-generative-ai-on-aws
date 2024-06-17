## Contextual Advertising with Generative AI on AWS

Contextual advertising is a form of targeted advertising where the advertisement is matched to the context of the webpage or media being consumed by the user. This process involves three key players: the publisher (website or content owner), the advertiser, and the consumer. Publishers provide the platform and content, while advertisers create ads tailored to the context. Consumers engage with the content, and relevant ads are displayed based on the context, creating a more personalized and relevant advertising experience.

One particularly challenging area of contextual advertising is inserting ads in media content for streaming on video on demand (VOD) platforms. This process traditionally relied on manual tagging, where human experts analyze the content and assign relevant keywords or categories. However, this approach is time-consuming, subjective, and may not capture the full context or nuances of the content. Traditional AI/ML solutions can automate this process, but they often require extensive training data and can be expensive and limited in their capabilities.

Generative AI, powered by large language models, offers a promising solution to this challenge. By leveraging the vast knowledge and contextual understanding of these models, broadcasters and content producers can automatically generate contextual insights and taxonomies for their media assets. This approach not only streamlines the process but also provides more accurate and comprehensive contextual understanding, enabling more effective ad targeting and monetization of media archives.

In this project, we will do a deep dive into one of the new features of the [Media2Cloud Guidance V4](https://aws.amazon.com/solutions/guidance/media2cloud-on-aws/), Scene and Ad break detection and contextual understanding of the Ad break. We will demonstrate step by step how to create contextual relevant insights and taxonomies for advertising using generative AI on AWS. This will allow broadcasters and content producers to monetize their media assets more effectively and extract greater value from their media archives. By harnessing the power of generative AI, they can unlock new revenue streams and deliver more personalized and engaging advertising experiences to their audiences.

### Watch the demo video

<a href="http://www.youtube.com/watch?feature=player_embedded&v=Ys9PMP1Gi7Ag
" target="_blank"><img src="https://www.youtube.com/watch?v=s9PMP1Gi7Ag/0.jpg" 
alt="IMAGE ALT TEXT HERE" width="240" height="180" border="10" /></a>

## Prerequisites to run the sample notebook

- You need to have an AWS account. Make sure your AWS identity has the requisite permissions, which include the ability to access Amazon Bedrock, Amazon SageMaker, and Amazon S3 access to upload files.
- You need to have permission to manage model access in Amazon Bedrock. This solution will need Claude 3 Sonnet and Claude 3 Haiku models.
- This notebook is tested using default Python3 kernel on Amazon SageMaker Studio. ml.m5.2xlarge CPU instance is recommended. Please reference the documentation on setting up a domain for Amazon SageMaker Studio.
- To run the notebook, you will need third-party libraries like ffmpeg, open-cv, and webvtt-py, make sure you follow the instruction and install them first before executing the code sections.
- The example video is Meridian, a short film downloaded from Netflix Open Content under Creative Commons Attribution 4.0 International Public License.

## Notebook configuration

The notebook for this sample runs well with the following SageMaker Studio configuration:

- Image: Data Science 3.0
- Instance Type: ml.t3.medium (Recommended)
- Python version: 3.10

## Security

See [CONTRIBUTING](CONTRIBUTING.md#security-issue-notifications) for more information.

## License

See the [LICENSE](./LICENSE) file.
