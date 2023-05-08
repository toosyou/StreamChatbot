FROM python:3.11.3

COPY example_in.txt /root/example_in.txt
COPY example_response.txt /root/example_response.txt
COPY secret.cfg /root/secret.cfg
COPY system_prompt.txt /root/system_prompt.txt
COPY chatgpt.py /root/chatgpt.py
RUN pip install --upgrade pip && \
    pip install flask && \
    pip install openai
    
ENTRYPOINT ["python"]
CMD ["/root/chatgpt.py"]